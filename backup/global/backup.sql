--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.9
-- Dumped by pg_dump version 9.6.9

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO peterdinh;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO peterdinh;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO peterdinh;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO peterdinh;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO peterdinh;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO peterdinh;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO peterdinh;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO peterdinh;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO peterdinh;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO peterdinh;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO peterdinh;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO peterdinh;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO peterdinh;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO peterdinh;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO peterdinh;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO peterdinh;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO peterdinh;

--
-- Name: website_account; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_account (
    id integer NOT NULL,
    username character varying(200) NOT NULL,
    email character varying(254) NOT NULL,
    password character varying(200) NOT NULL,
    name character varying(100) NOT NULL,
    birthday date,
    sex boolean NOT NULL,
    phone character varying(12),
    id_card character varying(15),
    address character varying(200),
    name_shop character varying(200),
    activity_account boolean NOT NULL,
    activity_merchant boolean NOT NULL,
    activity_advertiser boolean NOT NULL,
    q_post integer NOT NULL,
    q_vip integer NOT NULL,
    code_act_account character varying(60) NOT NULL,
    code_act_merchant character varying(60) NOT NULL,
    is_admin boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    is_lock boolean NOT NULL,
    token_ghtk character varying(100),
    code_act_ads character varying(60) NOT NULL
);


ALTER TABLE public.website_account OWNER TO peterdinh;

--
-- Name: website_account_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_account_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_account_id_seq OWNER TO peterdinh;

--
-- Name: website_account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_account_id_seq OWNED BY public.website_account.id;


--
-- Name: website_account_service; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_account_service (
    id integer NOT NULL,
    remain integer NOT NULL,
    account_id integer NOT NULL,
    service_id integer NOT NULL
);


ALTER TABLE public.website_account_service OWNER TO peterdinh;

--
-- Name: website_account_service_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_account_service_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_account_service_id_seq OWNER TO peterdinh;

--
-- Name: website_account_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_account_service_id_seq OWNED BY public.website_account_service.id;


--
-- Name: website_attribute; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_attribute (
    id integer NOT NULL,
    label character varying(200) NOT NULL,
    is_active boolean NOT NULL
);


ALTER TABLE public.website_attribute OWNER TO peterdinh;

--
-- Name: website_attribute_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_attribute_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_attribute_id_seq OWNER TO peterdinh;

--
-- Name: website_attribute_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_attribute_id_seq OWNED BY public.website_attribute.id;


--
-- Name: website_category; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_category (
    id integer NOT NULL,
    name_category character varying(200) NOT NULL,
    quantity integer NOT NULL,
    is_active boolean NOT NULL
);


ALTER TABLE public.website_category OWNER TO peterdinh;

--
-- Name: website_category_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_category_id_seq OWNER TO peterdinh;

--
-- Name: website_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_category_id_seq OWNED BY public.website_category.id;


--
-- Name: website_image; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_image (
    id integer NOT NULL,
    image_link character varying(100) NOT NULL,
    is_default boolean NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE public.website_image OWNER TO peterdinh;

--
-- Name: website_image_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_image_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_image_id_seq OWNER TO peterdinh;

--
-- Name: website_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_image_id_seq OWNED BY public.website_image.id;


--
-- Name: website_link_type; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_link_type (
    id integer NOT NULL,
    parent_product integer NOT NULL,
    product_id_id integer NOT NULL
);


ALTER TABLE public.website_link_type OWNER TO peterdinh;

--
-- Name: website_link_type_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_link_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_link_type_id_seq OWNER TO peterdinh;

--
-- Name: website_link_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_link_type_id_seq OWNED BY public.website_link_type.id;


--
-- Name: website_order; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_order (
    id integer NOT NULL,
    amount integer NOT NULL,
    email character varying(200) NOT NULL,
    address character varying(200) NOT NULL,
    phone character varying(12) NOT NULL,
    state character varying(1) NOT NULL,
    manner boolean NOT NULL,
    is_paid boolean NOT NULL,
    is_activity boolean NOT NULL,
    archive boolean NOT NULL,
    canceler_id integer,
    customer_id integer NOT NULL,
    note character varying(200),
    created timestamp with time zone NOT NULL,
    name character varying(200) NOT NULL
);


ALTER TABLE public.website_order OWNER TO peterdinh;

--
-- Name: website_order_detail; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_order_detail (
    id integer NOT NULL,
    quantity integer NOT NULL,
    price integer NOT NULL,
    state character varying(1) NOT NULL,
    confirm_of_merchant boolean NOT NULL,
    canceler_id integer,
    is_seen boolean NOT NULL,
    merchant_id integer NOT NULL,
    order_id integer NOT NULL,
    product_id integer NOT NULL,
    discount integer NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE public.website_order_detail OWNER TO peterdinh;

--
-- Name: website_order_detail_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_order_detail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_order_detail_id_seq OWNER TO peterdinh;

--
-- Name: website_order_detail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_order_detail_id_seq OWNED BY public.website_order_detail.id;


--
-- Name: website_order_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_order_id_seq OWNER TO peterdinh;

--
-- Name: website_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_order_id_seq OWNED BY public.website_order.id;


--
-- Name: website_post_product; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_post_product (
    id integer NOT NULL,
    quantity integer NOT NULL,
    expire timestamp with time zone NOT NULL,
    visable_vip boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    is_activity boolean NOT NULL,
    views integer NOT NULL,
    is_lock boolean NOT NULL,
    bought integer NOT NULL,
    creator_id_id integer NOT NULL,
    post_type_id integer NOT NULL,
    product_id_id integer NOT NULL
);


ALTER TABLE public.website_post_product OWNER TO peterdinh;

--
-- Name: website_post_product_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_post_product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_post_product_id_seq OWNER TO peterdinh;

--
-- Name: website_post_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_post_product_id_seq OWNED BY public.website_post_product.id;


--
-- Name: website_product; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_product (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    detail text,
    origin character varying(200) NOT NULL,
    type_product boolean NOT NULL,
    price integer NOT NULL,
    discount_percent integer NOT NULL,
    code character varying(200) NOT NULL,
    is_activity boolean NOT NULL,
    archive boolean NOT NULL,
    archive_at timestamp with time zone,
    account_created_id integer NOT NULL
);


ALTER TABLE public.website_product OWNER TO peterdinh;

--
-- Name: website_product_attribute; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_product_attribute (
    id integer NOT NULL,
    value character varying(200) NOT NULL,
    archive boolean NOT NULL,
    archive_at timestamp with time zone,
    lock boolean NOT NULL,
    attribute_id_id integer NOT NULL,
    product_id_id integer NOT NULL
);


ALTER TABLE public.website_product_attribute OWNER TO peterdinh;

--
-- Name: website_product_attribute_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_product_attribute_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_product_attribute_id_seq OWNER TO peterdinh;

--
-- Name: website_product_attribute_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_product_attribute_id_seq OWNED BY public.website_product_attribute.id;


--
-- Name: website_product_category; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_product_category (
    id integer NOT NULL,
    archive boolean NOT NULL,
    archive_at timestamp with time zone,
    lock boolean NOT NULL,
    category_id_id integer NOT NULL,
    product_id_id integer NOT NULL
);


ALTER TABLE public.website_product_category OWNER TO peterdinh;

--
-- Name: website_product_category_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_product_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_product_category_id_seq OWNER TO peterdinh;

--
-- Name: website_product_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_product_category_id_seq OWNED BY public.website_product_category.id;


--
-- Name: website_product_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_product_id_seq OWNER TO peterdinh;

--
-- Name: website_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_product_id_seq OWNED BY public.website_product.id;


--
-- Name: website_product_image; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_product_image (
    id integer NOT NULL,
    archive boolean NOT NULL,
    archive_at timestamp with time zone,
    image_id_id integer NOT NULL,
    product_id_id integer NOT NULL
);


ALTER TABLE public.website_product_image OWNER TO peterdinh;

--
-- Name: website_product_image_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_product_image_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_product_image_id_seq OWNER TO peterdinh;

--
-- Name: website_product_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_product_image_id_seq OWNED BY public.website_product_image.id;


--
-- Name: website_purchase_service; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_purchase_service (
    id integer NOT NULL,
    purchase_name character varying(200) NOT NULL,
    amount double precision,
    state integer NOT NULL,
    success_at timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    archive boolean NOT NULL,
    merchant_id_id integer NOT NULL,
    service_id_id integer NOT NULL
);


ALTER TABLE public.website_purchase_service OWNER TO peterdinh;

--
-- Name: website_purchase_service_ads; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_purchase_service_ads (
    id integer NOT NULL,
    purchase_name character varying(200) NOT NULL,
    amount integer NOT NULL,
    state character varying(1) NOT NULL,
    date_start timestamp with time zone,
    success_at timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    archive boolean NOT NULL,
    merchant_id_id integer NOT NULL,
    service_ads_id_id integer NOT NULL
);


ALTER TABLE public.website_purchase_service_ads OWNER TO peterdinh;

--
-- Name: website_purchase_service_ads_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_purchase_service_ads_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_purchase_service_ads_id_seq OWNER TO peterdinh;

--
-- Name: website_purchase_service_ads_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_purchase_service_ads_id_seq OWNED BY public.website_purchase_service_ads.id;


--
-- Name: website_purchase_service_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_purchase_service_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_purchase_service_id_seq OWNER TO peterdinh;

--
-- Name: website_purchase_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_purchase_service_id_seq OWNED BY public.website_purchase_service.id;


--
-- Name: website_rating; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_rating (
    id integer NOT NULL,
    num_of_star integer NOT NULL,
    comment character varying(2000),
    confirm_bought boolean NOT NULL,
    is_activity boolean NOT NULL,
    customer_id integer NOT NULL,
    merchant_id integer NOT NULL
);


ALTER TABLE public.website_rating OWNER TO peterdinh;

--
-- Name: website_rating_customer; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_rating_customer (
    id integer NOT NULL,
    num_of_star integer NOT NULL,
    confirm_bought boolean NOT NULL,
    is_activity boolean NOT NULL,
    customer_id integer NOT NULL,
    merchant_id integer NOT NULL
);


ALTER TABLE public.website_rating_customer OWNER TO peterdinh;

--
-- Name: website_rating_customer_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_rating_customer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_rating_customer_id_seq OWNER TO peterdinh;

--
-- Name: website_rating_customer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_rating_customer_id_seq OWNED BY public.website_rating_customer.id;


--
-- Name: website_rating_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_rating_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_rating_id_seq OWNER TO peterdinh;

--
-- Name: website_rating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_rating_id_seq OWNED BY public.website_rating.id;


--
-- Name: website_service; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_service (
    id integer NOT NULL,
    service_name character varying(200) NOT NULL,
    amount integer NOT NULL,
    value integer NOT NULL,
    quantity_product integer NOT NULL,
    created timestamp with time zone NOT NULL,
    day_limit integer NOT NULL,
    visable_vip boolean NOT NULL,
    is_active boolean NOT NULL,
    archive boolean NOT NULL,
    creator_id integer NOT NULL,
    canceler_id integer
);


ALTER TABLE public.website_service OWNER TO peterdinh;

--
-- Name: website_service_ads; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_service_ads (
    id integer NOT NULL,
    service_name character varying(200) NOT NULL,
    "position" character varying(200) NOT NULL,
    amount integer NOT NULL,
    created timestamp with time zone NOT NULL,
    day_limit integer NOT NULL,
    is_active boolean NOT NULL,
    archive boolean NOT NULL,
    creator_id integer NOT NULL,
    canceler_id integer
);


ALTER TABLE public.website_service_ads OWNER TO peterdinh;

--
-- Name: website_service_ads_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_service_ads_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_service_ads_id_seq OWNER TO peterdinh;

--
-- Name: website_service_ads_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_service_ads_id_seq OWNED BY public.website_service_ads.id;


--
-- Name: website_service_ads_post; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_service_ads_post (
    id integer NOT NULL,
    service_name character varying(200) NOT NULL,
    image_1 character varying(200) NOT NULL,
    image_1_url character varying(200) NOT NULL,
    image_1_content character varying(200) NOT NULL,
    image_2 character varying(200),
    image_2_url character varying(200),
    image_2_content character varying(200),
    image_3 character varying(200),
    image_3_url character varying(200),
    image_3_content character varying(200),
    state character varying(1) NOT NULL,
    customer_id_id integer NOT NULL,
    purchase_service_id_id integer NOT NULL
);


ALTER TABLE public.website_service_ads_post OWNER TO peterdinh;

--
-- Name: website_service_ads_post_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_service_ads_post_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_service_ads_post_id_seq OWNER TO peterdinh;

--
-- Name: website_service_ads_post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_service_ads_post_id_seq OWNED BY public.website_service_ads_post.id;


--
-- Name: website_service_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_service_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_service_id_seq OWNER TO peterdinh;

--
-- Name: website_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_service_id_seq OWNED BY public.website_service.id;


--
-- Name: website_tag; Type: TABLE; Schema: public; Owner: peterdinh
--

CREATE TABLE public.website_tag (
    id integer NOT NULL,
    tag_key character varying(200) NOT NULL,
    tag_value character varying(200) NOT NULL,
    tag_type integer NOT NULL,
    see integer NOT NULL,
    archive boolean NOT NULL,
    archive_at timestamp with time zone
);


ALTER TABLE public.website_tag OWNER TO peterdinh;

--
-- Name: website_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: peterdinh
--

CREATE SEQUENCE public.website_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_tag_id_seq OWNER TO peterdinh;

--
-- Name: website_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peterdinh
--

ALTER SEQUENCE public.website_tag_id_seq OWNED BY public.website_tag.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: website_account id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_account ALTER COLUMN id SET DEFAULT nextval('public.website_account_id_seq'::regclass);


--
-- Name: website_account_service id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_account_service ALTER COLUMN id SET DEFAULT nextval('public.website_account_service_id_seq'::regclass);


--
-- Name: website_attribute id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_attribute ALTER COLUMN id SET DEFAULT nextval('public.website_attribute_id_seq'::regclass);


--
-- Name: website_category id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_category ALTER COLUMN id SET DEFAULT nextval('public.website_category_id_seq'::regclass);


--
-- Name: website_image id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_image ALTER COLUMN id SET DEFAULT nextval('public.website_image_id_seq'::regclass);


--
-- Name: website_link_type id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_link_type ALTER COLUMN id SET DEFAULT nextval('public.website_link_type_id_seq'::regclass);


--
-- Name: website_order id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_order ALTER COLUMN id SET DEFAULT nextval('public.website_order_id_seq'::regclass);


--
-- Name: website_order_detail id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_order_detail ALTER COLUMN id SET DEFAULT nextval('public.website_order_detail_id_seq'::regclass);


--
-- Name: website_post_product id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_post_product ALTER COLUMN id SET DEFAULT nextval('public.website_post_product_id_seq'::regclass);


--
-- Name: website_product id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product ALTER COLUMN id SET DEFAULT nextval('public.website_product_id_seq'::regclass);


--
-- Name: website_product_attribute id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_attribute ALTER COLUMN id SET DEFAULT nextval('public.website_product_attribute_id_seq'::regclass);


--
-- Name: website_product_category id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_category ALTER COLUMN id SET DEFAULT nextval('public.website_product_category_id_seq'::regclass);


--
-- Name: website_product_image id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_image ALTER COLUMN id SET DEFAULT nextval('public.website_product_image_id_seq'::regclass);


--
-- Name: website_purchase_service id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_purchase_service ALTER COLUMN id SET DEFAULT nextval('public.website_purchase_service_id_seq'::regclass);


--
-- Name: website_purchase_service_ads id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_purchase_service_ads ALTER COLUMN id SET DEFAULT nextval('public.website_purchase_service_ads_id_seq'::regclass);


--
-- Name: website_rating id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_rating ALTER COLUMN id SET DEFAULT nextval('public.website_rating_id_seq'::regclass);


--
-- Name: website_rating_customer id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_rating_customer ALTER COLUMN id SET DEFAULT nextval('public.website_rating_customer_id_seq'::regclass);


--
-- Name: website_service id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_service ALTER COLUMN id SET DEFAULT nextval('public.website_service_id_seq'::regclass);


--
-- Name: website_service_ads id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_service_ads ALTER COLUMN id SET DEFAULT nextval('public.website_service_ads_id_seq'::regclass);


--
-- Name: website_service_ads_post id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_service_ads_post ALTER COLUMN id SET DEFAULT nextval('public.website_service_ads_post_id_seq'::regclass);


--
-- Name: website_tag id; Type: DEFAULT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_tag ALTER COLUMN id SET DEFAULT nextval('public.website_tag_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can view permission	1	view_permission
5	Can add group	2	add_group
6	Can change group	2	change_group
7	Can delete group	2	delete_group
8	Can view group	2	view_group
9	Can add user	3	add_user
10	Can change user	3	change_user
11	Can delete user	3	delete_user
12	Can view user	3	view_user
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add account	6	add_account
22	Can change account	6	change_account
23	Can delete account	6	delete_account
24	Can view account	6	view_account
25	Can add account_ service	7	add_account_service
26	Can change account_ service	7	change_account_service
27	Can delete account_ service	7	delete_account_service
28	Can view account_ service	7	view_account_service
29	Can add attribute	8	add_attribute
30	Can change attribute	8	change_attribute
31	Can delete attribute	8	delete_attribute
32	Can view attribute	8	view_attribute
33	Can add category	9	add_category
34	Can change category	9	change_category
35	Can delete category	9	delete_category
36	Can view category	9	view_category
37	Can add image	10	add_image
38	Can change image	10	change_image
39	Can delete image	10	delete_image
40	Can view image	10	view_image
41	Can add link_ type	11	add_link_type
42	Can change link_ type	11	change_link_type
43	Can delete link_ type	11	delete_link_type
44	Can view link_ type	11	view_link_type
45	Can add order	12	add_order
46	Can change order	12	change_order
47	Can delete order	12	delete_order
48	Can view order	12	view_order
49	Can add order_ detail	13	add_order_detail
50	Can change order_ detail	13	change_order_detail
51	Can delete order_ detail	13	delete_order_detail
52	Can view order_ detail	13	view_order_detail
53	Can add post_ product	14	add_post_product
54	Can change post_ product	14	change_post_product
55	Can delete post_ product	14	delete_post_product
56	Can view post_ product	14	view_post_product
57	Can add product	15	add_product
58	Can change product	15	change_product
59	Can delete product	15	delete_product
60	Can view product	15	view_product
61	Can add product_ attribute	16	add_product_attribute
62	Can change product_ attribute	16	change_product_attribute
63	Can delete product_ attribute	16	delete_product_attribute
64	Can view product_ attribute	16	view_product_attribute
65	Can add product_ category	17	add_product_category
66	Can change product_ category	17	change_product_category
67	Can delete product_ category	17	delete_product_category
68	Can view product_ category	17	view_product_category
69	Can add product_ image	18	add_product_image
70	Can change product_ image	18	change_product_image
71	Can delete product_ image	18	delete_product_image
72	Can view product_ image	18	view_product_image
73	Can add purchase_ service	19	add_purchase_service
74	Can change purchase_ service	19	change_purchase_service
75	Can delete purchase_ service	19	delete_purchase_service
76	Can view purchase_ service	19	view_purchase_service
77	Can add purchase_ service_ ads	20	add_purchase_service_ads
78	Can change purchase_ service_ ads	20	change_purchase_service_ads
79	Can delete purchase_ service_ ads	20	delete_purchase_service_ads
80	Can view purchase_ service_ ads	20	view_purchase_service_ads
81	Can add rating	21	add_rating
82	Can change rating	21	change_rating
83	Can delete rating	21	delete_rating
84	Can view rating	21	view_rating
85	Can add service	22	add_service
86	Can change service	22	change_service
87	Can delete service	22	delete_service
88	Can view service	22	view_service
89	Can add service_ ads	23	add_service_ads
90	Can change service_ ads	23	change_service_ads
91	Can delete service_ ads	23	delete_service_ads
92	Can view service_ ads	23	view_service_ads
93	Can add service_ ads_ post	24	add_service_ads_post
94	Can change service_ ads_ post	24	change_service_ads_post
95	Can delete service_ ads_ post	24	delete_service_ads_post
96	Can view service_ ads_ post	24	view_service_ads_post
97	Can add tag	25	add_tag
98	Can change tag	25	change_tag
99	Can delete tag	25	delete_tag
100	Can view tag	25	view_tag
101	Can add rating_ customer	26	add_rating_customer
102	Can change rating_ customer	26	change_rating_customer
103	Can delete rating_ customer	26	delete_rating_customer
104	Can view rating_ customer	26	view_rating_customer
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 104, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	auth	permission
2	auth	group
3	auth	user
4	contenttypes	contenttype
5	sessions	session
6	website	account
7	website	account_service
8	website	attribute
9	website	category
10	website	image
11	website	link_type
12	website	order
13	website	order_detail
14	website	post_product
15	website	product
16	website	product_attribute
17	website	product_category
18	website	product_image
19	website	purchase_service
20	website	purchase_service_ads
21	website	rating
22	website	service
23	website	service_ads
24	website	service_ads_post
25	website	tag
26	website	rating_customer
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 26, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2018-12-09 03:45:42.643447+00
2	contenttypes	0002_remove_content_type_name	2018-12-09 03:45:42.71926+00
3	auth	0001_initial	2018-12-09 03:45:44.440484+00
4	auth	0002_alter_permission_name_max_length	2018-12-09 03:45:44.673996+00
5	auth	0003_alter_user_email_max_length	2018-12-09 03:45:44.796242+00
6	auth	0004_alter_user_username_opts	2018-12-09 03:45:44.880408+00
7	auth	0005_alter_user_last_login_null	2018-12-09 03:45:44.985639+00
8	auth	0006_require_contenttypes_0002	2018-12-09 03:45:45.051483+00
9	auth	0007_alter_validators_add_error_messages	2018-12-09 03:45:45.133793+00
10	auth	0008_alter_user_username_max_length	2018-12-09 03:45:45.373072+00
11	auth	0009_alter_user_last_name_max_length	2018-12-09 03:45:45.495442+00
12	sessions	0001_initial	2018-12-09 03:45:46.106487+00
13	website	0001_initial	2018-12-09 03:45:52.094755+00
14	website	0002_auto_20181206_0306	2018-12-09 03:45:52.4484+00
15	website	0003_account_token_ghtk	2018-12-09 03:45:52.491627+00
16	website	0004_order_note	2018-12-09 03:45:52.591693+00
17	website	0005_remove_order_detail_version	2018-12-09 03:45:52.636418+00
18	website	0006_order_created	2018-12-09 03:45:52.869471+00
19	website	0007_auto_20181209_0345	2018-12-09 03:45:52.917293+00
20	website	0008_rating_customer	2018-12-10 04:34:09.389541+00
21	website	0009_order_detail_discount	2018-12-11 06:51:40.380341+00
22	website	0010_order_detail_post	2018-12-11 08:02:01.408192+00
23	website	0011_order_name	2018-12-12 02:22:23.767149+00
24	website	0012_auto_20181213_1307	2018-12-13 13:08:36.355551+00
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 24, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
gj03i1n9ropgopdzeft6drg1vix1lq7d	NThkZTQ3MjVlMWJmMGUyZGMwY2ZiZTJmYTQ2YWZhZjE5MGQxOTZkNTp7InVzZXIiOnsiaWQiOjEsImVtYWlsIjoibWVyY2hhbnRAbWFpbGluYXRvci5jb20iLCJyb2xlIjpbMSwyXX19	2018-12-23 03:51:18.828881+00
gurc42bobj3pggys9mcncjshfa0awen5	NThkZTQ3MjVlMWJmMGUyZGMwY2ZiZTJmYTQ2YWZhZjE5MGQxOTZkNTp7InVzZXIiOnsiaWQiOjEsImVtYWlsIjoibWVyY2hhbnRAbWFpbGluYXRvci5jb20iLCJyb2xlIjpbMSwyXX19	2018-12-24 03:19:09.150863+00
vxa2rvhhv8omicikkjivtwo276qo6gyn	NThkZTQ3MjVlMWJmMGUyZGMwY2ZiZTJmYTQ2YWZhZjE5MGQxOTZkNTp7InVzZXIiOnsiaWQiOjEsImVtYWlsIjoibWVyY2hhbnRAbWFpbGluYXRvci5jb20iLCJyb2xlIjpbMSwyXX19	2018-12-24 13:14:50.885624+00
7v5obvo1urvdz3iqqw9j2r189yu20lia	NThkZTQ3MjVlMWJmMGUyZGMwY2ZiZTJmYTQ2YWZhZjE5MGQxOTZkNTp7InVzZXIiOnsiaWQiOjEsImVtYWlsIjoibWVyY2hhbnRAbWFpbGluYXRvci5jb20iLCJyb2xlIjpbMSwyXX19	2018-12-25 02:44:28.864814+00
5wpbk7zwmwk2wdkry1ki73glxn2yqm7m	M2YxN2U5MWIwZmQ5ZDMzNmM0MDI3ZTkyYzcyMzA3MjJjY2JmYTBlODp7InVzZXIiOnsiaWQiOjIsImVtYWlsIjoiY3VzdG9tZXJAbWFpbGluYXRvci5jb20iLCJyb2xlIjpbMV19LCJDQVJUIjp7fX0=	2018-12-25 15:43:27.454209+00
b10ysse21kw3y2fesg68qnjgoj09w9w7	NThkZTQ3MjVlMWJmMGUyZGMwY2ZiZTJmYTQ2YWZhZjE5MGQxOTZkNTp7InVzZXIiOnsiaWQiOjEsImVtYWlsIjoibWVyY2hhbnRAbWFpbGluYXRvci5jb20iLCJyb2xlIjpbMSwyXX19	2018-12-25 17:23:08.622714+00
vf3cibkjytsztvl11u8vmfudh5upzilw	OWM3YTZkNzNkNmQ3ZWZhZjk3NzcyYTg5ZWU2MmQzYWNmMWY2NGJmODp7InVzZXIiOnsiaWQiOjIsImVtYWlsIjoiY3VzdG9tZXJAbWFpbGluYXRvci5jb20iLCJyb2xlIjpbMV19fQ==	2018-12-27 19:16:41.555041+00
mhk5rajabr6ltrg4gwuh9jtmsrsnecto	OWM3YTZkNzNkNmQ3ZWZhZjk3NzcyYTg5ZWU2MmQzYWNmMWY2NGJmODp7InVzZXIiOnsiaWQiOjIsImVtYWlsIjoiY3VzdG9tZXJAbWFpbGluYXRvci5jb20iLCJyb2xlIjpbMV19fQ==	2018-12-28 04:02:46.66736+00
\.


--
-- Data for Name: website_account; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_account (id, username, email, password, name, birthday, sex, phone, id_card, address, name_shop, activity_account, activity_merchant, activity_advertiser, q_post, q_vip, code_act_account, code_act_merchant, is_admin, created, is_lock, token_ghtk, code_act_ads) FROM stdin;
2	customer@mailinator.com	customer@mailinator.com	$pbkdf2-sha256$1200$MCZESIkxxjhnrBXCmBMihJByjvHe21uL0ZrTGsM4B8A$g4Bcnfeh6P5I0NlEiTYpEB4w6aDGTvuXFYNKorxJfRo	customer@mailinator.com	\N	f	\N	\N	\N	\N	t	f	f	0	0	rLe2z4cjE4pF3pFAYrCzkfx7rnEGXXW8O7VP6nt5		f	2018-12-11 06:28:37.328112+00	f	\N	
3	customer2@mailinator.com	customer2@mailinator.com	$pbkdf2-sha256$1200$.9.bcy4l5Nz735tTSund.1/LmfO.F0KI0Rrj/F/Lec8$xFvbClO0cV9L8bnxzQXuBJBw9wY1boD6nhrp92u77.E	customer2@mailinator.com	1990-12-30	f	\N	\N	\N	\N	f	f	f	0	0	fcjyqJHDw030lf0gSSeky5P6ebJkkeMhQLnTgbsu		f	2018-12-13 13:55:16.050949+00	f	\N	
5	customer3@mailinator.com	customer3@mailinator.com	$pbkdf2-sha256$1200$9X6P0VpLCSFESEmJcQ6hlDLm/D9HCKHUGiMEgFDqvVc$O64wZtgxl.v21eXVuwPe2rCqRSD36M7IYbWxHEuX2C8	customer3@mailinator.com	1990-12-30	f	\N	\N	\N	\N	f	f	f	0	0	ZEHiPTg1rQZSPdhokIpWk5uaHMZHYi9LDve96lGQ		f	2018-12-13 13:58:29.543384+00	f	\N	
6	customer4@mailinator.com	customer4@mailinator.com	$pbkdf2-sha256$1200$eo/x/h9jrBViDIEQgvBei7E2RshZKyVkzFkLwZizdk4$U1EpJxRU/U6OpILDftV7RnmaJPPKY8KkbkVLh7Ii9QA	customer4@mailinator.com	1990-12-30	f	\N	\N	\N	\N	f	f	f	0	0	avlmNeyvcCxHrC27MzFvzVJ8j6jHpMyLjHHLpiDU		f	2018-12-13 14:13:39.010652+00	f	\N	
8	customer5@mailinator.com	customer5@mailinator.com	$pbkdf2-sha256$1200$DkGIMeb8P8d47713bq0VAkAIAYBwjpGydq7VWouR8r4$H9H/LKCqjVf3cOhIy2GTwNXYt.Jovy37.eh/IiXtq7c	customer5@mailinator.com	1990-12-30	f	\N	\N	\N	\N	t	f	f	0	0	T0yuhAgxALXt8NFBEyjh6XLeYkSOGlUezxglx0zM		f	2018-12-13 14:16:11.532002+00	f	\N	
9	merchant2@mailinator.com	merchant2@mailinator.com	$pbkdf2-sha256$1200$w5jT2rvXOoeQ0tp7b.39v9d6bw0BoFQqBSDkHKNUinE$DXa.IsyFtcgiAmknqkWlZJ0pEdfDMXG2lQWQMKy50lA	merchant2@mailinator.com	\N	f	15151515151	merchant2	merchant2@mailinator.com	merchant2@mailinator.com	t	t	f	0	0		eE3kSjoFco10ohZpKAqG66TaaQKO3tf02N0G5BZm	f	2018-12-13 14:30:41.724353+00	f	\N	
12	ads1@mailinator.com	ads1@mailinator.com	$pbkdf2-sha256$1200$NYYQQihlrHWulbIW4nzP2VvLeY8xZgwhpFQqxdhbi9E$vb0p2PJ5EXt3YVrEgU8M1mZvLQo3QLVUmI4TIW0OcXw	ads1@mailinator.com	\N	f	123123	12312	ads@mailinator.com	ads@mailinator.com	t	f	t	0	0			f	2018-12-13 14:59:48.623894+00	f	\N	smZFueMZSPcx5fCWWPysZRKWkmJsEmub1tuofu9A
13	c@mailinator.com	c@mailinator.com	$pbkdf2-sha256$1200$6F1LCQGgNAaAkNL6X2tNKUWIUQohJISQ8v4/5xwDoPQ$iBudVcss1ZBrTlDg5VwMHxUWX4yrymM1bn77jRw0oMI	c@mailinator.com	1990-12-30	f	\N	\N	\N	\N	t	f	f	0	0	JjGUWjogNrxuRTfSxMwtxvTESAuQMODpYuQWGkQO		f	2018-12-13 16:09:01.832325+00	f	\N	
10	ads@mailinator.com	ads@mailinator.com	$pbkdf2-sha256$1200$Zuydk7JWCgEAgFDqPSekVIpx7n3vPWcsRSiFcG5NiZE$n6fRTdnvuBCy3MAqKscP/2./AJ7b7rH//LqkuhhCQAg	ads@mailinator.com	\N	f	123123	12312	ads@mailinator.com	ads@mailinator.com	t	f	f	0	0	yhhgVKRnavNBzuwJYHy0asMxKJJeeqOF52ysfKHa		f	2018-12-13 17:41:47.40789+00	f	\N	kHUYxT4H1iI51Lby9XRBfA2tzWVoTPvvZllGeP9U
14	merchant4@mailinator.com	merchant4@mailinator.com	$pbkdf2-sha256$1200$O4eQ0nqPkTLmHGOsVUophfB.7713rvXeO8c4B0CI0Vo$8rJlYuQyoElmy5hTN0.bZ7Amaciasyb68E8/VzMp6zE	merchant4@mailinator.com	\N	f	1231212121	merchan	merchant4@mailinator.com	merchant4@mailinator.com	f	f	f	0	0		QE3SBJNobqQ2ClMBNketdqhYdntt1bBTnRMnt0AG	f	2018-12-13 17:57:34.405155+00	f	\N	
15	merchant5@mailinator.com	merchant5@mailinator.com	$pbkdf2-sha256$1200$e./dO6e0VioFYOwdY8y5F8JYa62VEqKUMsY4J2TM2Vs$0twrfhgFRjR7/VLFuLa03r6wpEbId0aTbHj2PlYkSLs	merchant5@mailinator.com	\N	f	1231231231	12312312323	12312312	213213	t	t	f	0	0		KJrwCXmj1KqynF3SqSoBFojqbYBylS0jT1xXqSCf	f	2018-12-13 18:09:11.693954+00	f	\N	
1	merchant@mailinator.com	merchant@mailinator.com	$pbkdf2-sha256$29000$kxLC2LvXOqd0ztn7X6s1pg$5I3Wd4ETpD5yVwurOqm4FqrNAz/NlN7yjRD4jrOSASk	merchant@mailinator.com	1970-01-01	f	12312312312	12123123123	merchant@mailinator.com	merchant@mailinator.com	t	t	f	0	0	qwFKZskFPyYzB6mOiJ4R7u8DksEDu9GA0nUnWUCU	ryui7wV5n4sqXlb3VW1Xi8N7k1GDIcPeiTiser3Q	t	2018-12-13 17:38:45.877264+00	f	\N	
16	merchant6@mailinator.com	merchant6@mailinator.com	$pbkdf2-sha256$1200$5HzP2du719qb01qrtfbemxMihBCCEGIsBcCYU.odQwg$LGRq0ur.gVvgwFpEoqMNK/FHh681.3VVNJJca4nRf2I	merchant6@mailinator.com	\N	f	1231231233	12312312323	123123	33	t	t	f	0	0		OhrZTcXdkh2KjZYDdyZLzKnSiI1AtCA67ljknVOH	f	2018-12-13 18:11:44.552767+00	f	\N	
\.


--
-- Name: website_account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_account_id_seq', 16, true);


--
-- Data for Name: website_account_service; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_account_service (id, remain, account_id, service_id) FROM stdin;
2	0	1	2
3	0	1	3
1	12	1	1
4	0	16	1
5	0	16	2
6	0	16	3
\.


--
-- Name: website_account_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_account_service_id_seq', 6, true);


--
-- Data for Name: website_attribute; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_attribute (id, label, is_active) FROM stdin;
1	Ram	t
2	Man hinh	t
3	Camera	t
4	abc	t
\.


--
-- Name: website_attribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_attribute_id_seq', 4, true);


--
-- Data for Name: website_category; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_category (id, name_category, quantity, is_active) FROM stdin;
1	Ipad	0	t
\.


--
-- Name: website_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_category_id_seq', 1, true);


--
-- Data for Name: website_image; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_image (id, image_link, is_default, user_id_id) FROM stdin;
1	myAvatar (2)_wiVtUV2.png	f	1
2	unnamed (1).jpg	f	1
4	153796817958985578_FnAqhMJ.gif	f	1
6	iObQiPH_CQBDYwh.jpg	f	1
8	40371406_10209896151399936_5368938930815107072_n.jpg	f	1
9	iObQiPH_MNCgPyd.jpg	f	1
10	21645336802178_242_YipRVgA.jpg	f	1
11	e595b279547db723ee6c.jpg	f	1
\.


--
-- Name: website_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_image_id_seq', 11, true);


--
-- Data for Name: website_link_type; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_link_type (id, parent_product, product_id_id) FROM stdin;
1	1	2
2	1	3
3	1	4
4	1	5
5	1	6
6	1	7
7	1	8
8	9	10
9	9	11
10	9	12
11	9	13
12	9	14
13	9	15
14	16	17
\.


--
-- Name: website_link_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_link_type_id_seq', 14, true);


--
-- Data for Name: website_order; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_order (id, amount, email, address, phone, state, manner, is_paid, is_activity, archive, canceler_id, customer_id, note, created, name) FROM stdin;
1	18400	customer@mailinator.com	234324	2333333243	2	t	f	t	f	\N	2		2018-12-11 06:29:16.255208+00	peter
2	18400	customer@mailinator.com	2323	2342365561	2	t	f	t	f	\N	2		2018-12-11 14:50:53.518946+00	peter
3	18400	customer@mailinator.com	2323	1231651565	2	t	f	t	f	\N	2		2018-12-11 14:55:16.190576+00	peter
4	18400	customer@mailinator.com	2	1231231231	2	t	f	t	f	\N	2		2018-12-11 14:59:01.082292+00	peter
5	18400	customer@mailinator.com	2	1231231231	2	t	f	t	f	\N	2		2018-12-11 15:02:56.357822+00	peter
6	18400	customer@mailinator.com	2	1231231231	2	t	f	t	f	\N	2		2018-12-11 15:03:55.009551+00	peter
7	18400	customer@mailinator.com	2	1231231231	2	t	f	t	f	\N	2		2018-12-11 15:05:03.144437+00	peter
8	18400	customer@mailinator.com	2	1231231231	2	t	f	t	f	\N	2		2018-12-11 15:07:53.791483+00	peter
9	18400	customer@mailinator.com	21313	1231231232	2	t	f	t	f	\N	2		2018-12-11 15:08:47.628842+00	peter
10	18400	customer@mailinator.com	22333	2323232323	2	t	f	t	f	\N	2		2018-12-11 15:09:34.065251+00	peter
11	18400	customer@mailinator.com	2323	1231231231	2	t	f	t	f	\N	2		2018-12-11 15:13:18.68049+00	peter
12	18400	customer@mailinator.com	2323	1231231231	2	t	f	t	f	\N	2		2018-12-11 15:13:58.478726+00	peter
13	18400	customer@mailinator.com	2323	1231231231	2	t	f	t	f	\N	2		2018-12-11 15:23:56.815787+00	peter
14	18400	customer@mailinator.com	3	3242342343	2	t	f	t	f	\N	2		2018-12-11 15:24:49.637953+00	peter
15	18400	customer@mailinator.com	3	3242342343	2	t	f	t	f	\N	2		2018-12-11 15:25:10.837518+00	peter
16	18400	customer@mailinator.com	3	3242342343	2	t	f	t	f	\N	2		2018-12-11 15:25:59.900471+00	peter
17	18400	customer@mailinator.com	3	3242342343	2	t	f	t	f	\N	2		2018-12-11 15:26:28.081655+00	peter
18	18400	customer@mailinator.com	3	3242342343	2	t	f	t	f	\N	2		2018-12-11 15:26:50.144895+00	peter
19	18400	customer@mailinator.com	345	2234344353	2	t	f	t	f	\N	2		2018-12-11 15:27:27.407776+00	peter
20	18400	customer@mailinator.com	123123	1231231231	2	t	f	t	f	\N	2		2018-12-11 15:43:09.05172+00	peter
\.


--
-- Data for Name: website_order_detail; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_order_detail (id, quantity, price, state, confirm_of_merchant, canceler_id, is_seen, merchant_id, order_id, product_id, discount, post_id) FROM stdin;
1	1	18400	1	f	\N	f	1	1	17	20	3
8	1	18400	1	f	\N	f	1	18	17	20	3
9	1	18400	0	f	1	f	1	19	17	20	3
10	1	18400	1	f	\N	f	1	20	17	20	3
\.


--
-- Name: website_order_detail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_order_detail_id_seq', 10, true);


--
-- Name: website_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_order_id_seq', 20, true);


--
-- Data for Name: website_post_product; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_post_product (id, quantity, expire, visable_vip, created, is_activity, views, is_lock, bought, creator_id_id, post_type_id, product_id_id) FROM stdin;
2	20	2018-12-18 03:26:16.877961+00	t	2018-12-11 03:26:16.894728+00	f	0	t	0	1	1	9
1	15	2018-12-17 05:01:37.993859+00	t	2018-12-11 03:19:15.886588+00	f	0	t	0	1	1	1
3	20	2018-12-18 04:11:03.327111+00	t	2018-12-11 15:43:09.105281+00	t	0	f	4	1	1	16
\.


--
-- Name: website_post_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_post_product_id_seq', 3, true);


--
-- Data for Name: website_product; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_product (id, name, detail, origin, type_product, price, discount_percent, code, is_activity, archive, archive_at, account_created_id) FROM stdin;
2	abc	<p>323</p>\n	23	f	2324	2	adf .v1	t	t	2018-12-10 03:22:40.212316+00	1
3	abc .v1	<p>323</p>\n	30	f	2324	2	adf	t	t	2018-12-10 03:22:57.687628+00	1
4	abc .v1	<p>323</p>\n	45	f	2324	20	adf	t	t	2018-12-10 03:23:10.568085+00	1
5	abc .v1	<p>323</p>\n	45	f	2324	30	adf	t	t	2018-12-10 03:59:35.204508+00	1
6	abc .v1	<p>323</p>\n	45	f	2324	30	adf	t	t	2018-12-10 04:07:13.957134+00	1
7	abc .v1	<p>323</p>\n	45	f	2324	30	adf	t	t	2018-12-10 04:08:29.61314+00	1
8	abc .v1	<p>323</p>\n	45	f	2324	30	adf	t	f	\N	1
10	ads .v1	<p>223</p>\n	32	f	424234	33	sdsdf	t	t	2018-12-10 04:15:54.339554+00	1
11	ads .v1	<p>223</p>\n	32	f	424234	33	3222wư	t	t	2018-12-10 04:17:20.743955+00	1
12	ads	<p>223</p>\n	32	f	424234	33	232	t	t	2018-12-10 04:17:47.945388+00	1
13	ads .v1	<p>223</p>\n	32	f	23234	33	232	t	t	2018-12-10 04:18:09.244367+00	1
14	ads .v2	<p>223</p>\n	32	f	32424	33	232	t	t	2018-12-10 04:18:09.244367+00	1
15	ads	<p>223</p>\n	32	f	32424	33	232	t	f	\N	1
1	abc	<p>323</p>\n	45	t	2324	30	adf	t	t	2018-12-11 02:50:59.089516+00	1
9	ads	<p>223</p>\n	32	t	32424	33	232	f	t	2018-12-11 03:26:28.631283+00	1
17	Iphone .v1	<p>lksdjaodij</p>\n	32	f	23000	20	iph20	t	f	\N	1
16	Iphone	<p>lksdjaodij</p>\n	32	t	23000	20	iph20	t	f	\N	1
\.


--
-- Data for Name: website_product_attribute; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_product_attribute (id, value, archive, archive_at, lock, attribute_id_id, product_id_id) FROM stdin;
1	sf	f	\N	f	1	2
2	sf	f	\N	f	1	3
3	sf	f	\N	f	1	4
4	sf	f	\N	f	1	5
5	sf	f	\N	f	1	6
6	sf	f	\N	f	1	7
7	sf	f	\N	f	1	8
8	3	f	\N	f	1	10
9	3	f	\N	f	1	11
10	3	f	\N	f	1	12
11	3	f	\N	f	1	13
12	4	f	\N	f	1	14
13	4	f	\N	f	1	15
14	Chưa cập nhật	f	\N	f	2	2
15	Chưa cập nhật	f	\N	f	2	3
16	Chưa cập nhật	f	\N	f	2	4
17	Chưa cập nhật	f	\N	f	2	5
19	Chưa cập nhật	f	\N	f	2	6
21	Chưa cập nhật	f	\N	f	2	7
23	Chưa cập nhật	f	\N	f	2	8
25	Chưa cập nhật	f	\N	f	2	10
27	Chưa cập nhật	f	\N	f	2	11
29	Chưa cập nhật	f	\N	f	2	12
31	Chưa cập nhật	f	\N	f	2	13
33	Chưa cập nhật	f	\N	f	2	14
35	Chưa cập nhật	f	\N	f	2	15
39	Chưa cập nhật	f	\N	f	3	15
38	Chưa cập nhật	f	\N	f	3	14
37	Chưa cập nhật	f	\N	f	3	13
36	Chưa cập nhật	f	\N	f	3	12
34	Chưa cập nhật	f	\N	f	3	11
32	Chưa cập nhật	f	\N	f	3	10
30	Chưa cập nhật	f	\N	f	3	8
28	Chưa cập nhật	f	\N	f	3	7
26	Chưa cập nhật	f	\N	f	3	6
24	Chưa cập nhật	f	\N	f	3	5
22	Chưa cập nhật	f	\N	f	3	4
20	Chưa cập nhật	f	\N	f	3	3
18	Chưa cập nhật	f	\N	f	3	2
40	Chưa cập nhật	f	\N	f	4	2
41	Chưa cập nhật	f	\N	f	4	3
42	Chưa cập nhật	f	\N	f	4	4
43	Chưa cập nhật	f	\N	f	4	5
44	Chưa cập nhật	f	\N	f	4	6
45	Chưa cập nhật	f	\N	f	4	7
46	Chưa cập nhật	f	\N	f	4	8
47	Chưa cập nhật	f	\N	f	4	10
48	Chưa cập nhật	f	\N	f	4	11
49	Chưa cập nhật	f	\N	f	4	12
50	Chưa cập nhật	f	\N	f	4	13
51	Chưa cập nhật	f	\N	f	4	14
52	Chưa cập nhật	f	\N	f	4	15
53	e	f	\N	f	1	17
54	2	f	\N	f	2	17
55	4	f	\N	f	3	17
56	5	f	\N	f	4	17
\.


--
-- Name: website_product_attribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_product_attribute_id_seq', 56, true);


--
-- Data for Name: website_product_category; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_product_category (id, archive, archive_at, lock, category_id_id, product_id_id) FROM stdin;
1	t	2018-12-10 03:22:40.212316+00	f	1	1
2	t	2018-12-10 03:22:57.687628+00	f	1	1
3	t	2018-12-10 03:23:10.568085+00	f	1	1
4	t	2018-12-10 03:59:35.204508+00	f	1	1
5	t	2018-12-10 04:07:13.957134+00	f	1	1
6	t	2018-12-10 04:08:29.61314+00	f	1	1
7	f	\N	f	1	1
8	t	2018-12-10 04:15:54.339554+00	f	1	9
9	t	2018-12-10 04:17:20.743955+00	f	1	9
10	t	2018-12-10 04:17:47.945388+00	f	1	9
11	t	2018-12-10 04:18:09.244367+00	f	1	9
12	f	\N	f	1	9
13	f	\N	f	1	16
\.


--
-- Name: website_product_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_product_category_id_seq', 13, true);


--
-- Name: website_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_product_id_seq', 17, true);


--
-- Data for Name: website_product_image; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_product_image (id, archive, archive_at, image_id_id, product_id_id) FROM stdin;
1	t	2018-12-10 03:22:40.212316+00	1	1
2	t	2018-12-10 03:22:57.687628+00	1	1
3	t	2018-12-10 03:23:10.568085+00	1	1
4	t	2018-12-10 03:59:35.204508+00	1	1
5	t	2018-12-10 04:07:13.957134+00	6	1
6	t	2018-12-10 04:08:29.61314+00	8	1
7	f	\N	9	1
8	t	2018-12-10 04:15:54.339554+00	10	9
9	t	2018-12-10 04:17:20.743955+00	10	9
10	t	2018-12-10 04:17:47.945388+00	10	9
11	t	2018-12-10 04:18:09.244367+00	10	9
12	f	\N	10	9
13	f	\N	11	16
\.


--
-- Name: website_product_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_product_image_id_seq', 13, true);


--
-- Data for Name: website_purchase_service; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_purchase_service (id, purchase_name, amount, state, success_at, is_active, archive, merchant_id_id, service_id_id) FROM stdin;
1	PAY-54084487ML0333823LQG7FBI	6.45000000000000018	1	2018-12-10 05:01:07.356843+00	t	f	1	1
\.


--
-- Data for Name: website_purchase_service_ads; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_purchase_service_ads (id, purchase_name, amount, state, date_start, success_at, is_active, archive, merchant_id_id, service_ads_id_id) FROM stdin;
\.


--
-- Name: website_purchase_service_ads_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_purchase_service_ads_id_seq', 1, false);


--
-- Name: website_purchase_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_purchase_service_id_seq', 1, true);


--
-- Data for Name: website_rating; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_rating (id, num_of_star, comment, confirm_bought, is_activity, customer_id, merchant_id) FROM stdin;
1	3	\N	f	t	1	16
\.


--
-- Data for Name: website_rating_customer; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_rating_customer (id, num_of_star, confirm_bought, is_activity, customer_id, merchant_id) FROM stdin;
2	5	t	t	2	1
\.


--
-- Name: website_rating_customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_rating_customer_id_seq', 2, true);


--
-- Name: website_rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_rating_id_seq', 1, true);


--
-- Data for Name: website_service; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_service (id, service_name, amount, value, quantity_product, created, day_limit, visable_vip, is_active, archive, creator_id, canceler_id) FROM stdin;
1	Bạch kim	150000	15	20	2018-12-10 04:49:19.295965+00	7	t	t	f	1	\N
2	Vàng	1200000	10	20	2018-12-10 04:52:47.992575+00	7	t	f	f	1	\N
3	Vàng	120000	10	20	2018-12-10 04:53:16.340947+00	3	t	t	f	1	\N
\.


--
-- Data for Name: website_service_ads; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_service_ads (id, service_name, "position", amount, created, day_limit, is_active, archive, creator_id, canceler_id) FROM stdin;
\.


--
-- Name: website_service_ads_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_service_ads_id_seq', 1, false);


--
-- Data for Name: website_service_ads_post; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_service_ads_post (id, service_name, image_1, image_1_url, image_1_content, image_2, image_2_url, image_2_content, image_3, image_3_url, image_3_content, state, customer_id_id, purchase_service_id_id) FROM stdin;
\.


--
-- Name: website_service_ads_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_service_ads_post_id_seq', 1, false);


--
-- Name: website_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_service_id_seq', 3, true);


--
-- Data for Name: website_tag; Type: TABLE DATA; Schema: public; Owner: peterdinh
--

COPY public.website_tag (id, tag_key, tag_value, tag_type, see, archive, archive_at) FROM stdin;
1	3	1	1	0	t	2018-12-10 03:22:40.212316+00
2	34	1	1	0	t	2018-12-10 03:22:40.212316+00
3	3	1	1	0	t	2018-12-10 03:22:57.687628+00
4	34	1	1	0	t	2018-12-10 03:22:57.687628+00
5	3	1	1	0	t	2018-12-10 03:23:10.568085+00
6	34	1	1	0	t	2018-12-10 03:23:10.568085+00
7	3	1	1	0	t	2018-12-10 03:59:35.204508+00
8	34	1	1	0	t	2018-12-10 03:59:35.204508+00
9	3	1	1	0	t	2018-12-10 04:07:13.957134+00
10	34	1	1	0	t	2018-12-10 04:07:13.957134+00
11	3	1	1	0	t	2018-12-10 04:08:29.61314+00
12	34	1	1	0	t	2018-12-10 04:08:29.61314+00
13	3	1	1	0	f	\N
14	34	1	1	0	f	\N
15	2	16	1	0	f	\N
\.


--
-- Name: website_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peterdinh
--

SELECT pg_catalog.setval('public.website_tag_id_seq', 15, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: website_account website_account_email_key; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_account
    ADD CONSTRAINT website_account_email_key UNIQUE (email);


--
-- Name: website_account website_account_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_account
    ADD CONSTRAINT website_account_pkey PRIMARY KEY (id);


--
-- Name: website_account_service website_account_service_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_account_service
    ADD CONSTRAINT website_account_service_pkey PRIMARY KEY (id);


--
-- Name: website_account website_account_username_key; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_account
    ADD CONSTRAINT website_account_username_key UNIQUE (username);


--
-- Name: website_attribute website_attribute_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_attribute
    ADD CONSTRAINT website_attribute_pkey PRIMARY KEY (id);


--
-- Name: website_category website_category_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_category
    ADD CONSTRAINT website_category_pkey PRIMARY KEY (id);


--
-- Name: website_image website_image_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_image
    ADD CONSTRAINT website_image_pkey PRIMARY KEY (id);


--
-- Name: website_link_type website_link_type_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_link_type
    ADD CONSTRAINT website_link_type_pkey PRIMARY KEY (id);


--
-- Name: website_order_detail website_order_detail_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_order_detail
    ADD CONSTRAINT website_order_detail_pkey PRIMARY KEY (id);


--
-- Name: website_order website_order_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_order
    ADD CONSTRAINT website_order_pkey PRIMARY KEY (id);


--
-- Name: website_post_product website_post_product_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_post_product
    ADD CONSTRAINT website_post_product_pkey PRIMARY KEY (id);


--
-- Name: website_product_attribute website_product_attribute_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_attribute
    ADD CONSTRAINT website_product_attribute_pkey PRIMARY KEY (id);


--
-- Name: website_product_category website_product_category_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_category
    ADD CONSTRAINT website_product_category_pkey PRIMARY KEY (id);


--
-- Name: website_product_image website_product_image_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_image
    ADD CONSTRAINT website_product_image_pkey PRIMARY KEY (id);


--
-- Name: website_product website_product_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product
    ADD CONSTRAINT website_product_pkey PRIMARY KEY (id);


--
-- Name: website_purchase_service_ads website_purchase_service_ads_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_purchase_service_ads
    ADD CONSTRAINT website_purchase_service_ads_pkey PRIMARY KEY (id);


--
-- Name: website_purchase_service website_purchase_service_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_purchase_service
    ADD CONSTRAINT website_purchase_service_pkey PRIMARY KEY (id);


--
-- Name: website_rating_customer website_rating_customer_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_rating_customer
    ADD CONSTRAINT website_rating_customer_pkey PRIMARY KEY (id);


--
-- Name: website_rating website_rating_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_rating
    ADD CONSTRAINT website_rating_pkey PRIMARY KEY (id);


--
-- Name: website_service_ads website_service_ads_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_service_ads
    ADD CONSTRAINT website_service_ads_pkey PRIMARY KEY (id);


--
-- Name: website_service_ads_post website_service_ads_post_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_service_ads_post
    ADD CONSTRAINT website_service_ads_post_pkey PRIMARY KEY (id);


--
-- Name: website_service website_service_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_service
    ADD CONSTRAINT website_service_pkey PRIMARY KEY (id);


--
-- Name: website_tag website_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_tag
    ADD CONSTRAINT website_tag_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: website_account_email_2224b0ca_like; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_account_email_2224b0ca_like ON public.website_account USING btree (email varchar_pattern_ops);


--
-- Name: website_account_service_account_id_56267cd3; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_account_service_account_id_56267cd3 ON public.website_account_service USING btree (account_id);


--
-- Name: website_account_service_service_id_53e03611; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_account_service_service_id_53e03611 ON public.website_account_service USING btree (service_id);


--
-- Name: website_account_username_b7945dab_like; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_account_username_b7945dab_like ON public.website_account USING btree (username varchar_pattern_ops);


--
-- Name: website_image_user_id_id_be620ec9; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_image_user_id_id_be620ec9 ON public.website_image USING btree (user_id_id);


--
-- Name: website_link_type_product_id_id_b0300c69; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_link_type_product_id_id_b0300c69 ON public.website_link_type USING btree (product_id_id);


--
-- Name: website_order_customer_id_e1325c64; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_order_customer_id_e1325c64 ON public.website_order USING btree (customer_id);


--
-- Name: website_order_detail_merchant_id_53d411e1; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_order_detail_merchant_id_53d411e1 ON public.website_order_detail USING btree (merchant_id);


--
-- Name: website_order_detail_order_id_c60e1227; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_order_detail_order_id_c60e1227 ON public.website_order_detail USING btree (order_id);


--
-- Name: website_order_detail_post_id_d0630e8c; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_order_detail_post_id_d0630e8c ON public.website_order_detail USING btree (post_id);


--
-- Name: website_order_detail_product_id_e467e8e4; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_order_detail_product_id_e467e8e4 ON public.website_order_detail USING btree (product_id);


--
-- Name: website_post_product_creator_id_id_76436dc0; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_post_product_creator_id_id_76436dc0 ON public.website_post_product USING btree (creator_id_id);


--
-- Name: website_post_product_post_type_id_2e0fc9e5; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_post_product_post_type_id_2e0fc9e5 ON public.website_post_product USING btree (post_type_id);


--
-- Name: website_post_product_product_id_id_d62082d6; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_post_product_product_id_id_d62082d6 ON public.website_post_product USING btree (product_id_id);


--
-- Name: website_product_account_created_id_de464db0; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_product_account_created_id_de464db0 ON public.website_product USING btree (account_created_id);


--
-- Name: website_product_attribute_attribute_id_id_4546df39; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_product_attribute_attribute_id_id_4546df39 ON public.website_product_attribute USING btree (attribute_id_id);


--
-- Name: website_product_attribute_product_id_id_e5e923de; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_product_attribute_product_id_id_e5e923de ON public.website_product_attribute USING btree (product_id_id);


--
-- Name: website_product_category_category_id_id_91d4f89a; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_product_category_category_id_id_91d4f89a ON public.website_product_category USING btree (category_id_id);


--
-- Name: website_product_category_product_id_id_e4f959a9; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_product_category_product_id_id_e4f959a9 ON public.website_product_category USING btree (product_id_id);


--
-- Name: website_product_image_image_id_id_035e34b7; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_product_image_image_id_id_035e34b7 ON public.website_product_image USING btree (image_id_id);


--
-- Name: website_product_image_product_id_id_82d25a86; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_product_image_product_id_id_82d25a86 ON public.website_product_image USING btree (product_id_id);


--
-- Name: website_purchase_service_ads_merchant_id_id_cc93068d; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_purchase_service_ads_merchant_id_id_cc93068d ON public.website_purchase_service_ads USING btree (merchant_id_id);


--
-- Name: website_purchase_service_ads_service_ads_id_id_7cf89745; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_purchase_service_ads_service_ads_id_id_7cf89745 ON public.website_purchase_service_ads USING btree (service_ads_id_id);


--
-- Name: website_purchase_service_merchant_id_id_6b95262b; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_purchase_service_merchant_id_id_6b95262b ON public.website_purchase_service USING btree (merchant_id_id);


--
-- Name: website_purchase_service_service_id_id_5daf978e; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_purchase_service_service_id_id_5daf978e ON public.website_purchase_service USING btree (service_id_id);


--
-- Name: website_rating_customer_customer_id_51e029ee; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_rating_customer_customer_id_51e029ee ON public.website_rating_customer USING btree (customer_id);


--
-- Name: website_rating_customer_id_ac5279ff; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_rating_customer_id_ac5279ff ON public.website_rating USING btree (customer_id);


--
-- Name: website_rating_customer_merchant_id_0dbf9560; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_rating_customer_merchant_id_0dbf9560 ON public.website_rating_customer USING btree (merchant_id);


--
-- Name: website_rating_merchant_id_f5bfaa46; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_rating_merchant_id_f5bfaa46 ON public.website_rating USING btree (merchant_id);


--
-- Name: website_service_ads_post_customer_id_id_26db606b; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_service_ads_post_customer_id_id_26db606b ON public.website_service_ads_post USING btree (customer_id_id);


--
-- Name: website_service_ads_post_purchase_service_id_id_e7c1b6ac; Type: INDEX; Schema: public; Owner: peterdinh
--

CREATE INDEX website_service_ads_post_purchase_service_id_id_e7c1b6ac ON public.website_service_ads_post USING btree (purchase_service_id_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_account_service website_account_serv_account_id_56267cd3_fk_website_a; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_account_service
    ADD CONSTRAINT website_account_serv_account_id_56267cd3_fk_website_a FOREIGN KEY (account_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_account_service website_account_serv_service_id_53e03611_fk_website_s; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_account_service
    ADD CONSTRAINT website_account_serv_service_id_53e03611_fk_website_s FOREIGN KEY (service_id) REFERENCES public.website_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_image website_image_user_id_id_be620ec9_fk_website_account_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_image
    ADD CONSTRAINT website_image_user_id_id_be620ec9_fk_website_account_id FOREIGN KEY (user_id_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_link_type website_link_type_product_id_id_b0300c69_fk_website_product_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_link_type
    ADD CONSTRAINT website_link_type_product_id_id_b0300c69_fk_website_product_id FOREIGN KEY (product_id_id) REFERENCES public.website_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_order website_order_customer_id_e1325c64_fk_website_account_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_order
    ADD CONSTRAINT website_order_customer_id_e1325c64_fk_website_account_id FOREIGN KEY (customer_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_order_detail website_order_detail_merchant_id_53d411e1_fk_website_account_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_order_detail
    ADD CONSTRAINT website_order_detail_merchant_id_53d411e1_fk_website_account_id FOREIGN KEY (merchant_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_order_detail website_order_detail_order_id_c60e1227_fk_website_order_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_order_detail
    ADD CONSTRAINT website_order_detail_order_id_c60e1227_fk_website_order_id FOREIGN KEY (order_id) REFERENCES public.website_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_order_detail website_order_detail_post_id_d0630e8c_fk_website_p; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_order_detail
    ADD CONSTRAINT website_order_detail_post_id_d0630e8c_fk_website_p FOREIGN KEY (post_id) REFERENCES public.website_post_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_order_detail website_order_detail_product_id_e467e8e4_fk_website_product_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_order_detail
    ADD CONSTRAINT website_order_detail_product_id_e467e8e4_fk_website_product_id FOREIGN KEY (product_id) REFERENCES public.website_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_post_product website_post_product_creator_id_id_76436dc0_fk_website_a; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_post_product
    ADD CONSTRAINT website_post_product_creator_id_id_76436dc0_fk_website_a FOREIGN KEY (creator_id_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_post_product website_post_product_post_type_id_2e0fc9e5_fk_website_s; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_post_product
    ADD CONSTRAINT website_post_product_post_type_id_2e0fc9e5_fk_website_s FOREIGN KEY (post_type_id) REFERENCES public.website_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_post_product website_post_product_product_id_id_d62082d6_fk_website_p; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_post_product
    ADD CONSTRAINT website_post_product_product_id_id_d62082d6_fk_website_p FOREIGN KEY (product_id_id) REFERENCES public.website_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_product website_product_account_created_id_de464db0_fk_website_a; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product
    ADD CONSTRAINT website_product_account_created_id_de464db0_fk_website_a FOREIGN KEY (account_created_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_product_attribute website_product_attr_attribute_id_id_4546df39_fk_website_a; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_attribute
    ADD CONSTRAINT website_product_attr_attribute_id_id_4546df39_fk_website_a FOREIGN KEY (attribute_id_id) REFERENCES public.website_attribute(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_product_attribute website_product_attr_product_id_id_e5e923de_fk_website_p; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_attribute
    ADD CONSTRAINT website_product_attr_product_id_id_e5e923de_fk_website_p FOREIGN KEY (product_id_id) REFERENCES public.website_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_product_category website_product_cate_category_id_id_91d4f89a_fk_website_c; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_category
    ADD CONSTRAINT website_product_cate_category_id_id_91d4f89a_fk_website_c FOREIGN KEY (category_id_id) REFERENCES public.website_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_product_category website_product_cate_product_id_id_e4f959a9_fk_website_p; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_category
    ADD CONSTRAINT website_product_cate_product_id_id_e4f959a9_fk_website_p FOREIGN KEY (product_id_id) REFERENCES public.website_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_product_image website_product_imag_product_id_id_82d25a86_fk_website_p; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_image
    ADD CONSTRAINT website_product_imag_product_id_id_82d25a86_fk_website_p FOREIGN KEY (product_id_id) REFERENCES public.website_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_product_image website_product_image_image_id_id_035e34b7_fk_website_image_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_product_image
    ADD CONSTRAINT website_product_image_image_id_id_035e34b7_fk_website_image_id FOREIGN KEY (image_id_id) REFERENCES public.website_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_purchase_service website_purchase_ser_merchant_id_id_6b95262b_fk_website_a; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_purchase_service
    ADD CONSTRAINT website_purchase_ser_merchant_id_id_6b95262b_fk_website_a FOREIGN KEY (merchant_id_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_purchase_service_ads website_purchase_ser_merchant_id_id_cc93068d_fk_website_a; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_purchase_service_ads
    ADD CONSTRAINT website_purchase_ser_merchant_id_id_cc93068d_fk_website_a FOREIGN KEY (merchant_id_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_purchase_service_ads website_purchase_ser_service_ads_id_id_7cf89745_fk_website_s; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_purchase_service_ads
    ADD CONSTRAINT website_purchase_ser_service_ads_id_id_7cf89745_fk_website_s FOREIGN KEY (service_ads_id_id) REFERENCES public.website_service_ads(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_purchase_service website_purchase_ser_service_id_id_5daf978e_fk_website_s; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_purchase_service
    ADD CONSTRAINT website_purchase_ser_service_id_id_5daf978e_fk_website_s FOREIGN KEY (service_id_id) REFERENCES public.website_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_rating_customer website_rating_custo_customer_id_51e029ee_fk_website_a; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_rating_customer
    ADD CONSTRAINT website_rating_custo_customer_id_51e029ee_fk_website_a FOREIGN KEY (customer_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_rating_customer website_rating_custo_merchant_id_0dbf9560_fk_website_a; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_rating_customer
    ADD CONSTRAINT website_rating_custo_merchant_id_0dbf9560_fk_website_a FOREIGN KEY (merchant_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_rating website_rating_customer_id_ac5279ff_fk_website_account_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_rating
    ADD CONSTRAINT website_rating_customer_id_ac5279ff_fk_website_account_id FOREIGN KEY (customer_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_rating website_rating_merchant_id_f5bfaa46_fk_website_account_id; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_rating
    ADD CONSTRAINT website_rating_merchant_id_f5bfaa46_fk_website_account_id FOREIGN KEY (merchant_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_service_ads_post website_service_ads__customer_id_id_26db606b_fk_website_a; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_service_ads_post
    ADD CONSTRAINT website_service_ads__customer_id_id_26db606b_fk_website_a FOREIGN KEY (customer_id_id) REFERENCES public.website_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: website_service_ads_post website_service_ads__purchase_service_id__e7c1b6ac_fk_website_p; Type: FK CONSTRAINT; Schema: public; Owner: peterdinh
--

ALTER TABLE ONLY public.website_service_ads_post
    ADD CONSTRAINT website_service_ads__purchase_service_id__e7c1b6ac_fk_website_p FOREIGN KEY (purchase_service_id_id) REFERENCES public.website_purchase_service_ads(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

